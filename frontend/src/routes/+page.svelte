<script>
	import Card from '$lib/Card.svelte';

	let data = {
		count: 2,
		next: 'http://localhost:8000/api/v1/projects/?page=2',
		previous: null,
		results: [
			{
				id: 1,
				company_id: 3,
				company: 'Wells Fargo Bank (FKA Wachovia Bank)',
				title: 'Implement open banking',
				description: 'example of description',
				creation_date: '2024-09-13',
				expiration_date: '2025-09-13',
				state: 'active',
				token: 'USDT',
				tokens_limit: 4000
			},
			{
				id: 2,
				company_id: 4,
				company: 'Compañia Nutresa',
				title: 'Optimize the supply chain',
				description: 'example of description',
				state: 'finished',
				creation_date: '2024-09-13',
				expiration_date: '2025-09-13',
				token: 'AVAX',
				tokens_limit: 2000
			}
		]
	};
	// let colorState = {
	// 	active: '#22c55e',
	// 	complete: '#6b7280'
	// };
</script>

<!-- component -->
<div class="h-screen w-full bg-white relative flex overflow-hidden">
	<div class="w-full h-full flex flex-col justify-between">
		<!-- Main -->
		<main class="max-w-full h-full flex relative overflow-y-hidden">
			<!-- Container -->
			<div
				class="h-full w-full m-4 flex flex-wrap items-start justify-start rounded-tl grid-flow-col auto-cols-max gap-4"
			>
				<!-- Container -->
				<div class="w-96 rounded-lg flex-shrink-0 flex-grow mb-4">
					<Card />
				</div>
				<div class="w-96 rounded-lg flex-shrink-0 flex-grow mb-4">
					<Card />
				</div>
				<div class="w-96 rounded-lg flex-shrink-0 flex-grow mb-4">
					<Card />
				</div>
				<div class="w-96 rounded-lg flex-shrink-0 flex-grow mb-4">
					<Card />
				</div>
				<div class="w-96 rounded-lg flex-shrink-0 flex-grow mb-4">
					<Card />
				</div>
				<div class="w-96 rounded-lg flex-shrink-0 flex-grow mb-4">
					<Card />
				</div>

				<!-- <div class="w-96 h-60 rounded-lg flex-shrink-0 flex-grow bg-gray-400"></div>
				<div class="w-96 h-60 rounded-lg flex-shrink-0 flex-grow bg-gray-400"></div>
				<div class="w-96 h-60 rounded-lg flex-shrink-0 flex-grow bg-gray-400"></div>
				<div class="w-96 h-60 rounded-lg flex-shrink-0 flex-grow bg-gray-400"></div>
				<div class="w-96 h-60 rounded-lg flex-shrink-0 flex-grow bg-gray-400"></div>
				<div class="w-96 h-60 rounded-lg flex-shrink-0 flex-grow bg-gray-400"></div>
				<div class="w-96 h-60 rounded-lg flex-shrink-0 flex-grow bg-gray-400"></div>
				<div class="w-96 h-60 rounded-lg flex-shrink-0 flex-grow bg-gray-400"></div> -->
			</div>
		</main>
	</div>
</div>

<style>
</style>
