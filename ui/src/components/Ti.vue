<template>
    <div id="Ti">
        <div>
            <span>
                #{{ props.name }}
            </span>
            <div @click="$emit('deletethis')"><svg t="1790938710119" class="icon" viewBox="0 0 1024 800" version="1.1"
                    xmlns="http://www.w3.org/2000/svg" p-id="27152" width="16" height="16">
                    <path
                        d="M608 112a112 112 0 0 1 111.616 102.784l0.384 9.216v16h144a48 48 0 0 1 6.528 95.552l-6.528 0.448h-48v400a176 176 0 0 1-165.248 175.68L640 912H384a176 176 0 0 1-175.68-165.248L208 736V336H160a48 48 0 0 1-47.552-41.472L112 288a48 48 0 0 1 41.472-47.552L160 240h144V224a112 112 0 0 1 102.784-111.616L416 112h192z m112 224h-416v400c0 41.408 31.488 75.52 71.808 79.616L384 816h256a80 80 0 0 0 79.616-71.808l0.384-8.192V336zM416 432a48 48 0 0 1 47.552 41.472l0.448 6.528v192a48 48 0 0 1-95.552 6.528L368 672v-192a48 48 0 0 1 48-48z m192 0a48 48 0 0 1 48 48v192a48 48 0 1 1-96 0v-192a48 48 0 0 1 48-48z m0-224h-192a16 16 0 0 0-15.552 12.352L400 224v16h224V224a16 16 0 0 0-12.352-15.552L608 208z"
                        fill="#d81e06" p-id="27153"></path>
                </svg></div>
        </div>
    </div>
</template>
<script setup name="Zx">
let props = defineProps(["name"]);
</script>
<style lang="scss" scoped>
#Ti {
    width: fit-content;
    max-width: calc(100vw - 145px);
    height: 20px;
    padding-top: 5px;
    padding-bottom: 15px;
    padding-left: 5px;

    &>div {
        &>span{
            overflow: hidden;
            text-overflow: ellipsis;
            text-wrap-mode: nowrap;
        }
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 5px;
        border-radius: 8px;
        font-weight: bold;
        color: #623a44;
        background-color: #ff8fab;

        &>div {
            padding-left: 10px;
            cursor: pointer;

        }
    }
}
</style>