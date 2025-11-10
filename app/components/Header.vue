<template>
	<div class="bg-default-secondary h-12 flex flex-row justify-between items-center border-default-primary border-b-2">
	<header>
		<a href="/" class="px-4 my-auto">
			<p class="text-white">GG.EZ</p>
		</a>
	</header>
	<Switch v-model="sessionStore.displaySR" :class="sessionStore.displaySR ? 'bg-blue-600' : 'bg-gray-200'" class="relative inline-flex h-6 w-11 items-center rounded-full">
		<span class="sr-only">Enable notifications</span>
		<span :class="sessionStore.displaySR ? 'translate-x-6' : 'translate-x-1'" class="inline-block h-4 w-4 transform rounded-full bg-white transition" />
	</Switch>
	</div>
</template>

<script setup lang="ts">
import { ref } from "vue"
import { Switch } from "@headlessui/vue"
const sessionStore = useSessionStore()
</script>
