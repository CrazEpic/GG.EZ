<template>
	<div class="border-ionia-primary border-2 bg-ionia-secondary">
		<p class="text-white">Discover your closest professional counterparts</p>
		<div class="flex flex-row w-full justify-evenly">
            <div>
                <img :src="pro_1_img" @click="choosePro(pro_1)" :class="`aspect-square w-24 ${pro_1 == proChosen ? 'border-2 border-ionia-primary' : ''}`" style="border-radius: 50%;"></img>
                <p class="text-white">{{ pro_1 }}</p>
            </div>
            <div>
                <img :src="pro_2_img" @click="choosePro(pro_2)" :class="`aspect-square w-24 ${pro_2 == proChosen ? 'border-2 border-ionia-primary' : ''}`" style="border-radius: 50%;"></img>
                <p class="text-white">{{ pro_2 }}</p>
            </div>
            <div>
                <img :src="pro_3_img" @click="choosePro(pro_3)" :class="`aspect-square w-24 ${pro_3 == proChosen ? 'border-2 border-ionia-primary' : ''}`" style="border-radius: 50%;"></img>
                <p class="text-white">{{ pro_3 }}</p>
            </div>
        </div>
	</div>
</template>

<script setup lang="ts">
const props = defineProps({
	pro_1: {
		type: String,
		required: true,
	},
    pro_1_img: {
        type: String,
		required: true,
	},
	pro_2: {
		type: String,
		required: true,
	},
    pro_2_img: {
        type: String,
        required: true,
    },
	pro_3: {
		type: String,
		required: true,
	},
    pro_3_img: {
        type: String,
        required: true,
    },
})

const emit = defineEmits(["choose_pro"])

const proChosen = ref("")
const choosePro = (pro: string) => {
    if (proChosen.value === pro) {
        proChosen.value = ""
        emit("choose_pro", "")
        return
    }
    proChosen.value = pro
    emit("choose_pro", pro)
}
</script>
