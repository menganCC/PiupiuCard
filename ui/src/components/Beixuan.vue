<template>
    <div id="beixuanbox">
        <div>
            <Beixuanlist v-for="(index, i) in jsonall.data.data.alternate_greetings" :data="index" :key="i"
                @setindex="ref.id = i" @delete="jsonall.data.data.alternate_greetings.splice(i, 1)" :i="i"
                :down="ref" />
            <div id="addbeixuan" @click="jsonall.data.data.alternate_greetings.push('new')">
                <svg t="1791038066251" class="icon" viewBox="0 0 1024 1024" version="1.1"
                    xmlns="http://www.w3.org/2000/svg" p-id="11254" width="32" height="32">
                    <path
                        d="M811.625 631.625h-59.90625v119.90625H631.90625v59.90625h119.8125v119.90625h59.90625V811.4375h119.90625v-59.90625H811.625z"
                        fill="#ff8fab" p-id="11255"></path>
                    <path
                        d="M561.03125 899.375c0-17.34375-14.0625-31.5-31.5-31.5H301.34375c-80.8125 0-146.625-65.8125-146.625-146.625V300.96875c0-80.8125 65.71875-146.625 146.625-146.625h420.375c80.8125 0 146.625 65.8125 146.625 146.625v223.875c0 17.34375 14.0625 31.5 31.5 31.5s31.5-14.0625 31.5-31.5V300.96875C931.25 185.375 837.3125 91.34375 721.71875 91.34375H301.34375C185.75 91.34375 91.71875 185.375 91.71875 300.875v420.28125c0 115.5 94.03125 209.53125 209.625 209.53125h228.1875c17.4375 0.09375 31.5-13.96875 31.5-31.3125z"
                        fill="#ff8fab" p-id="11256"></path>
                </svg>
            </div>
        </div>
        <div>
            <monaco :options="{
                wordWrap: 'on',
                automaticLayout: true

            }" v-model:value="jsonall.data.data.alternate_greetings[ref.id]"
                style="border-radius: 8px;overflow: hidden;" theme="vs-dark" language="text" />
        </div>
    </div>
</template>
<script setup name="beixuan">
import monaco from "monaco-editor-vue3"
import Beixuanlist from "./Beixuanlist.vue";
import { reactive } from "vue";
import { jsonall } from "../main.js";
let ref = reactive({
    id: 0
})
</script>
<style lang="scss">
#beixuanbox {
    display: grid;
    width: 100%;
    height: 100%;
    max-height: 100%;
    grid-template-columns: 150px 1fr;

    &>div:nth-child(1) {
        overflow-x: hidden;
        overflow-y: scroll;
        min-height: 0%;
        display: flex;
        padding-top: 4px;
        gap: 4px;
        flex-wrap: wrap;
        align-content: first baseline;
        justify-content: center;
    }

    #addbeixuan {
        width: 32px;
        height: 32px;
    }
}
</style>