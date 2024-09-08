<script>
	// Add your component logic here
</script>

<section class=" py-1 bg-blueGray-50">
	<div class="w-full lg:w-8/12 px-4 mx-auto mt-6">
		<div
			class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-100 border-0"
		>
			<div class="rounded-t bg-white mb-0 px-6 py-6">
				<div class="text-center flex justify-between">
					<!-- <h6 class="text-blueGray-700 text-xl font-bold">My account</h6>s -->
					<div>
						<button
							class="bg-red-500 text-white active:bg-pink-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
							type="button"
						>
							Cancelar
						</button>
						<button
							class="bg-green-500 text-white active:bg-pink-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
							type="button"
						>
							Guardar
						</button>
					</div>
				</div>
			</div>
			<div class="flex-auto px-4 lg:px-10 py-10 pt-0">
				<form>
					<h6 class="text-blueGray-400 text-sm mt-3 mb-6 font-bold uppercase">User Information</h6>
					<div class="flex flex-wrap">
						<div class="w-full lg:w-6/12 px-4">
							<div class="relative w-full mb-3">
								<label class="block uppercase text-blueGray-600 text-xs font-bold mb-2">
									Compañia
								</label>
								<input
									type="text"
									class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
									placeholder="ingrese el nombre de la compañia"
									value="Postobon"
								/>
							</div>
						</div>
						<div class="w-full lg:w-6/12 px-4">
							<div class="relative w-full mb-3">
								<label class="block uppercase text-blueGray-600 text-xs font-bold mb-2">
									titulo del anuncio
								</label>
								<input
									type="email"
									class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
									value="Optimización de la cadena de suministro usando IA"
									placeholder="ingrese el titulo del anuncio"
								/>
							</div>
						</div>
						<div class="w-full lg:w-6/12 px-4">
							<div class="relative w-full mb-3">
								<label class="block uppercase text-blueGray-600 text-xs font-bold mb-2">
									Descripción del anuncio
								</label>
								<textarea
									class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
									rows="4"
								>
								</textarea>
							</div>
						</div>
						<div class="w-full lg:w-6/12 px-4">
							<div class="relative w-full mb-3">
								<label class="block uppercase text-blueGray-600 text-xs font-bold mb-2">
									Resumen de proyecto
								</label>
								<input
									type="file"
									class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
								/>
							</div>
						</div>
					</div>

					<hr class="mt-6 border-b-1 border-blueGray-300" />

					<h6 class="text-blueGray-400 text-sm mt-3 mb-6 font-bold uppercase">
						Fecha de inicio y expiración
					</h6>
					<div class="flex flex-wrap">
						<div class="w-full lg:w-12/12 px-4">
							<div class="relative w-full mb-3">
								<label class="block uppercase text-blueGray-600 text-xs font-bold mb-2">
									Fecha de inicio
								</label>
								<input
									type="date"
									class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
									value="Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09"
								/>
							</div>
						</div>

						<div class="w-full lg:w-4/12 px-4">
							<div class="relative w-full mb-3">
								<label class="block uppercase text-blueGray-600 text-xs font-bold mb-2">
									Fecha de expiración
								</label>
								<input
									type="date"
									class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
									value="New York"
								/>
							</div>
						</div>
					</div>

					<hr class="mt-6 border-b-1 border-blueGray-300" />

					<h6 class="text-blueGray-400 text-sm mt-3 mb-6 font-bold uppercase">Recompensas</h6>
					<div class="flex flex-wrap">
						<div class="w-full lg:w-4/12 px-4">
							<div class="relative w-full mb-3">
								<label class="block uppercase text-blueGray-600 text-xs font-bold mb-2">
									Token
								</label>
								<select
									class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
								>
									<option value="USDT">USDT</option>
									<option value="AVAX">AVAX</option>
								</select>
							</div>
						</div>
						<div class="w-full lg:w-6/12 px-4">
							<div class="relative w-full mb-3">
								<label class="block uppercase text-blueGray-600 text-xs font-bold mb-2">
									Limite de tokens
								</label>
								<input
									type="number"
									class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
									placeholder="ingrese el limite de tokens"
									value="2000"
								/>
							</div>
						</div>
					</div>
				</form>
			</div>
		</div>
	</div>
</section>

<style>
	/* Add your component styles here */
</style>
