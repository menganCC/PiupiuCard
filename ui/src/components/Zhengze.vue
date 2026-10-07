<template>
    <div id="zhengzebox">
        <div>
            <div>
                <span>启用角色正则
                    <fuxuankuang_zhengze_all />
                </span>
                <span>关闭后,该角色聊天内容的正则替换不会生效</span>
            </div>
            <div>
                <zhengzelist @delete="jsonall.data.data.extensions.piupiu_regex.scripts.splice(i, 1)"
                    @setindex="re.index = i" :index="re"
                    v-for="(index, i) in jsonall.data.data.extensions.piupiu_regex.scripts" :key="i" :v="i" />
                <div id="addzz" @click="addzz">
                    <span>添加正则规则</span>
                </div>
            </div>
        </div>
        <div>
            <div>
                <div>
                    <span>查找正则</span>
                </div>
                <div>
                    <monaco :options="{
            wordWrap: 'on',
            automaticLayout:true
                    }" v-model:value="findRegex" style="border-radius: 8px;overflow: hidden;" theme="vs-dark"
                        language="text" />
                </div>
            </div>
            <div>
                <div>
                    <span>替换内容</span>
                </div>
                <div>
                    <monaco :options="{
            wordWrap: 'on',
            automaticLayout:true
                    }" v-model:value="replaceString" style="border-radius: 8px;overflow: hidden;" theme="vs-dark"
                        language="text" />
                </div>
            </div>
        </div>
    </div>
</template>
<script setup name="zhengze">
import monaco from 'monaco-editor-vue3'
import Zhengzelist from './Zhengzelist.vue';
import Fuxuankuang_zhengze_all from './Fuxuankuang_zhengze_all.vue';
import { reactive } from 'vue';
import { computed } from 'vue';
import { jsonall } from '../main.js';
let re = reactive({
    index: 0
})
const currentScript = computed(() => jsonall?.data?.data?.extensions?.piupiu_regex?.scripts?.[re.index] ?? null)

let get_uuid = async () => {
    const id = await pywebview.api.get_uuid()
    return id
}
// 带 setter 的 computed：读安全，写安全
const findRegex = computed({
    get: () => currentScript.value?.findRegex ?? '',
    set: (val) => {
        if (currentScript.value) { currentScript.value.findRegex = val; jsonall.data.data.extensions.regex_scripts=jsonall.data.data.extensions.piupiu_regex.scripts}
    }
})

const replaceString = computed({
    get: () => currentScript.value?.replaceString ?? '',
    set: (val) => {
        if (currentScript.value) {currentScript.value.replaceString = val; jsonall.data.data.extensions.regex_scripts=jsonall.data.data.extensions.piupiu_regex.scripts}
    }
})
let addzz = async () => {
    let add = JSON.parse(`{"disabled":false,"findRegex":"","id":"${await get_uuid()}","markdownOnly":true,"maxDepth":null,"minDepth":null,"placement":[1,2],"promptOnly":false,"replaceString":"","runOnEdit":false,"scriptName":"正则new","substituteRegex":0,"trimStrings":[]}`);
    jsonall.data.data.extensions.piupiu_regex.scripts.push(add);
    jsonall.data.data.extensions.regex_scripts=jsonall.data.data.extensions.piupiu_regex.scripts
}
</script>
<style lang="scss" scoped>
#addzz {
    width: 175px;
    height: 50px;
    border-style: dashed;
    border-radius: 8px;
    justify-content: center;
    align-items: center;
    border-color: #ff8fab;
    display: flex;

    &>span {
        color: #ff8fab;
    }
}

#zhengzebox {
    display: grid;
    grid-template-columns: 200px 1fr;
    height: 100%;

    &>div:nth-child(1) {
        overflow-x: hidden;
        overflow-y: scroll;
        justify-self: center;
        width: 190px;
        display: flex;
        flex-wrap: wrap;
        align-content: flex-start;
        justify-content: center;

        &>div:nth-child(1) {
            margin-top: 5px;
            margin-bottom: 5px;
            display: grid;
            height: 50px;
            align-items: center;
            grid-template-rows: 23px 1fr;
            background-color: #3d3239;
            border-radius: 8px;
            padding: 5px;

            &>span:nth-child(1) {
                font-size: 14px;
                display: flex;
                font-weight: bold;
                gap: 5px;
            }

            &>span:nth-child(2) {
                color: #ff8fab;
                align-self: self-start;
                font-size: 10px;
            }
        }

        &>div:nth-child(2) {
            display: flex;
            gap: 5px;
            flex-wrap: wrap;
        }
    }

    &>div:nth-child(2) {
        display: grid;
        height: calc(100vh - 30px - 50px);
        grid-template-rows: repeat(2, 1fr);

        &>div {
            display: grid;
            // border-style: dashed;
            grid-template-rows: 30px 1fr;
            gap: 5px;

            &>div:nth-child(1) {
                padding-top: 10px;

                &>span {
                    height: 30px;
                    padding: 8px;
                    border-color: #ff8fab;
                    color: #ff8fab;
                    border-left-style: solid;
                }
            }

            &>div {
                height: 100%;
            }
        }
    }
}
</style>