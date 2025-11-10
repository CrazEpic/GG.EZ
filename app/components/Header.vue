<template>
	<div class="bg-default-secondary h-12 flex flex-row justify-between items-center border-default-primary border-b-2">
		<header>
			<a href="/" class="px-4 my-auto">
				<p class="text-white">GG.EZ</p>
			</a>
		</header>
		<Switch
			v-model="sessionStore.displaySR"
			:class="sessionStore.displaySR ? 'bg-default-secondary' : 'bg-freljord-secondary'"
			class="relative inline-flex w-32 items-center justify-center rounded-full text-white border-default-primary border-2 cursor-pointer"
		>
			{{ sessionStore.displaySR ? "SR" : "ARAM" }}
			<!-- <span class="sr-only">Enable notifications</span> -->
			<!-- <span :class="sessionStore.displaySR ? 'translate-x-6' : 'translate-x-1'" class="inline-block h-4 w-4 transform rounded-full bg-white transition" /> -->
		</Switch>
	</div>
</template>

<script setup lang="ts">
import { Switch } from "@headlessui/vue"
const sessionStore = useSessionStore()
</script>
