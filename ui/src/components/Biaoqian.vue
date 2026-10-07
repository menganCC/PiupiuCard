<template>
    <div id="Biqoqian">
        <Ti v-for="(index,i) in jsonall.data.data.tags" :name="index" :key="i" @deletethis="jsonall.data.data.tags.splice(i,1)"/>
        <div class="add">
            <div>
                <input type="text" name="" id="addtab">
            </div>
            <div @click="addtab()"><svg t="1790939944651" class="icon" viewBox="0 0 1024 1024" version="1.1"
                    xmlns="http://www.w3.org/2000/svg" p-id="28239" width="16" height="16">
                    <path
                        d="M945.230769 472.615385L551.384615 472.615385 551.384615 78.769231 472.615385 78.769231 472.615385 472.615385 78.769231 472.615385 78.769231 551.384615 472.615385 551.384615 472.615385 945.230769 551.384615 945.230769 551.384615 551.384615 945.230769 551.384615Z"
                        fill="#ffffff" p-id="28240"></path>
                </svg></div>
        </div>
    </div>
</template>
<script setup name="Biaoqian">
import Ti from './Ti.vue';
import { jsonall } from '../main.js';
let addtab=()=>{
jsonall.data.data.tags.push(`${document.querySelector("#addtab").value}`)
}
</script>
<style lang="scss" scoped>
#Biqoqian {
    width: 100%;
    height: 100%;
    display: flex;
    flex-wrap: wrap;
    align-content: flex-start;
    &>.add {

        display: flex;

        &>div:nth-child(1) {
            &>input {
                padding-left: 3px;
                width: 100%;
                border-style: none;
                background-color: transparent;
            }

            margin-left: 5px;
            margin-top: 5px;
            width: 150px;
            background-color: #494b53;
            height: 35px;
            border-radius: 8px;
            border-style: solid;
            border-width: 1px;
            border-color: #cdcdce;
            display: grid;
            grid-template-columns: 1fr 35px;
        }

        &>div:nth-child(2) {
            display: flex;
            margin-top: 5px;
            margin-left: 5px;
            width: 35px;
            height: 35px;
            background-color: #ff8fab;
            border-radius: 8px;
            justify-content: center;
            align-items: center;
        }
    }
}
</style>