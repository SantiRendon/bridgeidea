
from rest_framework import viewsets

from API.serializers import SolutionSerializer
from API.models import Solution

from web3 import Web3

from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

avalanche_url = "https://api.avax-test.network/ext/bc/C/rpc"
web3 = Web3(Web3.HTTPProvider(avalanche_url))

# Dirección del contrato desplegado y ABI
contract_address = "0xd6ed6f49e95f27ae39ef3d017b3a6198037fff82"
checksum_address = Web3.to_checksum_address(contract_address)
contract_abi = [
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_solutionData",
				"type": "string"
			}
		],
		"name": "addSolution",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "bytes32",
				"name": "solutionHash",
				"type": "bytes32"
			}
		],
		"name": "SolutionAdded",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_hash",
				"type": "string"
			}
		],
		"name": "getSolution",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]


# Instanciar el contrato
contract = web3.eth.contract(address=checksum_address, abi=contract_abi)

@permission_classes([AllowAny])
class SolutionViewSet(viewsets.ModelViewSet):
    
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    
    def perform_create(self, serializer):
        """Inserta la solución en la base de datos y realiza la transacción para guardar en la
        blockchain la información del proyecto

        Args:
            serializer (_type_): _description_
        """
        obj = serializer.save()
        
        account = '0x8165C54A74b6a567C38a62F5076dCd4179Dc96De'  # Dirección desde donde se hará la transacción
        checksum_address_2 = Web3.to_checksum_address(account)
        private_key = '0xc7571a9316bcdd5afa6c0d1e996cf1c97c2720ad3ad9834f9b761d705f02b72d'     # Clave privada para firmar la transacción
        
        transaction = contract.functions.addProject(obj._data).build_transaction({
                'from': checksum_address_2,
                'nonce': web3.eth.get_transaction_count(checksum_address_2),
                'gas': 200000,
                'gasPrice': web3.to_wei('20', 'gwei')
            })
        
        # Firmar la transacción
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key)
        
        # Enviar la transacción
        txn_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)

        # Esperar a que se confirme
        txn_receipt = web3.eth.wait_for_transaction_receipt(txn_hash)
        
        obj.hash_id = txn_receipt.transactionHash
        obj.save()
    