<script>
	// Add your component logic here
	export let company_id = 1;
	export let title = 'Implement open banking';
	export let description = 'example of description';
	export let creation_date = '2024-09-13';
	export let expiration_date = '2025-04-23';
	export let state = 'complete';
	export let token = 'USDT';
	export let tokens_limit = 4000;
	export let colorState = '#22c55e';

	// let colorState = {
	// 	active: '#22c55e',
	// 	complete: '#6b7280'
	// };
</script>

<a href="/project" class="block rounded-lg p-4 shadow-sm shadow-indigo-100">
	<img
		alt="alternative text"
		src="https://images.unsplash.com/photo-1613545325278-f24b0cae1224?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80"
		class="h-56 w-full rounded-md object-cover"
	/>

	<svg
		id="Filled_Circle_24"
		width="24"
		height="24"
		viewBox="0 0 24 24"
		xmlns="http://www.w3.org/2000/svg"
		xmlns:xlink="http://www.w3.org/1999/xlink"
		style="position: relative; bottom: 190px; left: 5px;"
		><rect width="24" height="24" stroke="none" fill={colorState} opacity="0" />

		<g transform="matrix(1 0 0 1 12 12)">
			<path
				style="stroke: none; stroke-width: 1; stroke-dasharray: none; stroke-linecap: butt; stroke-dashoffset: 0; stroke-linejoin: miter; stroke-miterlimit: 4; fill: {colorState}; fill-rule: nonzero; opacity: 1; position: absolute; "
				transform=" translate(-12, -12)"
				d="M 12 2 C 6.477152501692066 2 2 6.477152501692066 2 12 C 2 17.522847498307932 6.477152501692066 22 12 22 C 17.522847498307932 22 22 17.522847498307932 22 12 C 22 6.477152501692066 17.522847498307932 2 12 2 z"
				stroke-linecap="round"
			/>
		</g>
	</svg>

	<div class="mt-2">
		<dl>
			<div>
				<dt class="sr-only">Titulo del proyecto</dt>

				<dd class="font-medium">{title} | {tokens_limit} {token}</dd>
			</div>
			<!-- <div>
				<dt class="sr-only">Token</dt>
				<dd class="text-sm text-gray-500"></dd>
			</div> -->
		</dl>

		<dl>
			<div>
				<dt class="sr-only">Descripción</dt>
				<dd class="text-lg text-gray-500">{description}</dd>
			</div>
		</dl>

		<div class="mt-6 flex items-center gap-8 text-xs">
			<div class="sm:inline-flex sm:shrink-0 sm:items-center sm:gap-2">
				<svg
					id="Calendar_Plus_24"
					width="24"
					height="24"
					viewBox="0 0 24 24"
					xmlns="http://www.w3.org/2000/svg"
					xmlns:xlink="http://www.w3.org/1999/xlink"
					><rect width="24" height="24" stroke="none" fill="#4338ca" opacity="0" />

					<g transform="matrix(1 0 0 1 12 12)">
						<path
							style="stroke: none; stroke-width: 1; stroke-dasharray: none; stroke-linecap: butt; stroke-dashoffset: 0; stroke-linejoin: miter; stroke-miterlimit: 4; fill: #4338ca; fill-rule: nonzero; opacity: 1;"
							transform=" translate(-12, -11)"
							d="M 7 1 C 6.448 1 6 1.448 6 2 L 6 3 L 5 3 C 3.895 3 3 3.895 3 5 L 3 19 C 3 20.105 3.895 21 5 21 L 19 21 C 20.105 21 21 20.105 21 19 L 21 5 C 21 3.895 20.105 3 19 3 L 18 3 L 18 2 C 18 1.448 17.552 1 17 1 C 16.448 1 16 1.448 16 2 L 16 3 L 8 3 L 8 2 C 8 1.448 7.552 1 7 1 z M 5 8 L 19 8 L 19.001953 19 L 5 19 L 5 8 z M 12 11 C 11.448 11 11 11.448 11 12 L 11 13 L 10 13 C 9.448 13 9 13.448 9 14 C 9 14.552 9.448 15 10 15 L 11 15 L 11 16 C 11 16.552 11.448 17 12 17 C 12.552 17 13 16.552 13 16 L 13 15 L 14 15 C 14.552 15 15 14.552 15 14 C 15 13.448 14.552 13 14 13 L 13 13 L 13 12 C 13 11.448 12.552 11 12 11 z"
							stroke-linecap="round"
						/>
					</g>
				</svg>

				<div class="mt-1.5 sm:mt-0">
					<p class="text-gray-500">Fecha de creación</p>

					<p class="font-medium">{creation_date}</p>
				</div>
			</div>

			<div class="sm:inline-flex sm:shrink-0 sm:items-center sm:gap-2">
				<!-- <svg
					class="size-4 text-indigo-700"
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					viewBox="0 0 24 24"
					stroke="currentColor"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"
					/>
				</svg> -->
				<svg
					width="24"
					height="24"
					viewBox="0 0 24 24"
					xmlns="http://www.w3.org/2000/svg"
					xmlns:xlink="http://www.w3.org/1999/xlink"
					><rect width="24" height="24" stroke="none" fill="#4338ca" opacity="0" />

					<g transform="matrix(0.4 0 0 0.4 12 12)">
						<path
							style="stroke: none; stroke-width: 1; stroke-dasharray: none; stroke-linecap: butt; stroke-dashoffset: 0; stroke-linejoin: miter; stroke-miterlimit: 4; fill: #4338ca; fill-rule: nonzero; opacity: 1;"
							transform=" translate(-25.02, -25)"
							d="M 15 0 C 6.753906 0 0 6.753906 0 15 C 0 23.246094 6.753906 30 15 30 C 15.796875 30 16.628906 29.882813 17.34375 29.78125 C 17.726563 29.769531 18.066406 29.539063 18.222656 29.1875 C 18.378906 28.835938 18.320313 28.429688 18.074219 28.136719 C 17.824219 27.84375 17.433594 27.71875 17.0625 27.8125 C 16.375 27.910156 15.605469 28 15 28 C 7.84375 28 2 22.15625 2 15 C 2 7.84375 7.84375 2 15 2 C 20.855469 2 25.863281 5.90625 27.4375 11.28125 C 27.59375 11.816406 28.152344 12.125 28.6875 11.96875 C 29.222656 11.8125 29.53125 11.253906 29.375 10.71875 C 27.550781 4.496094 21.746094 0 15 0 Z M 14.90625 4.96875 C 14.863281 4.976563 14.820313 4.988281 14.78125 5 C 14.316406 5.105469 13.988281 5.523438 14 6 L 14 13.5 C 13.519531 13.824219 13.1875 14.378906 13.1875 15 C 13.1875 15.105469 13.234375 15.214844 13.25 15.3125 L 9.59375 19 C 9.296875 19.242188 9.160156 19.628906 9.246094 20.003906 C 9.332031 20.375 9.625 20.667969 9.996094 20.753906 C 10.371094 20.839844 10.757813 20.703125 11 20.40625 L 14.6875 16.75 C 14.785156 16.765625 14.894531 16.8125 15 16.8125 C 15.992188 16.8125 16.8125 15.992188 16.8125 15 C 16.8125 14.378906 16.480469 13.824219 16 13.5 L 16 6 C 16.011719 5.710938 15.894531 5.433594 15.6875 5.238281 C 15.476563 5.039063 15.191406 4.941406 14.90625 4.96875 Z M 29.5 14.25 C 29.15625 14.25 28.804688 14.378906 28.625 14.6875 L 9.125 48.5 C 8.945313 48.808594 8.945313 49.191406 9.125 49.5 C 9.304688 49.808594 9.644531 50 10 50 L 49 50 C 49.007813 50 49.023438 50 49.03125 50 C 49.585938 50 50.03125 49.554688 50.03125 49 C 50.03125 48.75 49.933594 48.519531 49.78125 48.34375 L 30.375 14.6875 C 30.195313 14.378906 29.84375 14.25 29.5 14.25 Z M 28.5 27 L 30.40625 27 C 30.605469 27 30.6875 27.113281 30.6875 27.3125 L 30.6875 38.6875 C 30.6875 38.886719 30.605469 39 30.40625 39 L 28.5 39 C 28.300781 39 28.1875 38.886719 28.1875 38.6875 L 28.1875 27.3125 C 28.1875 27.113281 28.300781 27 28.5 27 Z M 28.5 41.3125 L 30.5 41.3125 C 30.699219 41.3125 30.8125 41.394531 30.8125 41.59375 L 30.8125 43.6875 C 30.8125 43.886719 30.699219 44 30.5 44 L 28.5 44 C 28.300781 44 28.1875 43.886719 28.1875 43.6875 L 28.1875 41.59375 C 28.1875 41.394531 28.300781 41.3125 28.5 41.3125 Z"
							stroke-linecap="round"
						/>
					</g>
				</svg>

				<div class="mt-1.5 sm:mt-0">
					<p class="text-gray-500">Fecha de expiración</p>

					<p class="font-medium">{expiration_date}</p>
				</div>
			</div>

			<!-- <div class="sm:inline-flex sm:shrink-0 sm:items-center sm:gap-2">
				<div class="mt-1.5 sm:mt-0">
					<p class="text-gray-500">Bedroom</p>

					<p class="font-medium">4 rooms</p>
				</div>
			</div> -->
		</div>
	</div>
</a>

<style>
	/* Add your component styles here */
</style>
