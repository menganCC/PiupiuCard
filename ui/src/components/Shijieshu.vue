<template>
    <div id="shijieshubox">
        <div>
            <div>
                <div>启用世界书<div>
                        <Fuxuankuang_shijieshu :v="true" />
                    </div>
                </div>
                <span class="beizhu">关闭后所有条目都将消失</span>
            </div>
            <div>
                <div>一键常驻<div>
                        <Fuxuankuang_shijieshu :v="false" />
                    </div>
                </div>
                <span class="beizhu">开启后所有条目将忽略各自的常驻设置，全部强制常驻</span>
            </div>
            <div>
                <div><span>书名</span><input type="text" v-model="jsonall.data.data.character_book.name"></div>
                <div><span>描述</span><input type="text" v-model="jsonall.data.data.character_book.description"></div>
                <div><span>扫描深度</span><input type="text" v-model="jsonall.data.data.character_book.scan_depth"></div>
                <div><span>Token预算</span>
                    <Fuxuankuang_token /><input type="text"
                        :class="{ enable_input: jsonall.data.data.character_book.token_budget_enabled == true ? false : true }"
                        v-model="jsonall.data.data.character_book.token_budget">
                </div>
            </div>
            <div>
                <Shijieshulist v-for="(index, i) in jsonall.data.data.character_book.entries"
                    @delete="jsonall.data.data.character_book.entries.splice(i, 1)" :key="i" :v="i" :down="ref"
                    @setindex="ref.index = i"
                    @setdownindex="ref.downindex == i ? ref.downindex = -1 : ref.downindex = i" />
                <div id="addzhishi" @click="addjson" style="width: 100%;">添加知识条目</div>
            </div>
        </div>
        <div>
            <monaco v-model:value="content" :options="{
            wordWrap: 'on',
            automaticLayout:true
            }" style="border-radius: 8px;overflow: hidden;" theme="vs-dark" language="text" />
        </div>
    </div>
</template>
<script setup name="shijieshu">
import { computed } from "vue";
import monaco from "monaco-editor-vue3"
import Fuxuankuang_token from "./Fuxuankuang_token.vue";
import Fuxuankuang_shijieshu from "./Fuxuankuang_shijieshu.vue";
import Shijieshulist from "./Shijieshulist.vue";
import { jsonall } from "../main.js";
import { reactive } from "vue";
let iscontent = computed(() => jsonall?.data?.data?.character_book?.entries?.[ref.index] ?? null)
let content = computed({
    get: () => iscontent.value?.content ?? '',
    set: (s) => { if (iscontent.value) iscontent.value.content = s }
})
let ref = reactive({
    index: 0,
    downindex: -1
})
const addjson = () => {
    jsonall.data.data.character_book.entries.push(JSON.parse('{"comment":"","constant":false,"content":"φ(゜▽゜*)♪","enabled":true,"extensions":{"position":1},"insertion_order":20,"keys":[],"name":"new","position":"after_character_definition","priority":666}'));
}
</script>
<style lang="scss" scoped>
#shijieshubox {
    display: grid;
    width: 100%;
    height: 100%;
    grid-template-columns: 200px 1fr;

    &>div:nth-child(1) {
        padding-top: 5px;
        display: flex;
        flex-wrap: wrap;
        gap: 5px;
        align-content: flex-start;
        justify-content: center;
        overflow-y: scroll;

        &>div {
            &:nth-child(1) {
                position: sticky;
                top: 0;
            }

            &:nth-child(1),
            &:nth-child(2) {
                &>div {
                    font-size: 14px;
                    font-weight: bold;
                    padding-left: 5px;
                    gap: 5px;
                    // color: #64473f;
                    align-items: center;
                    display: flex;
                    align-self: baseline;
                }

                background-color: #3d3239;
                border-radius: 8px;
                display: grid;
                gap: 3px;
                grid-template-rows: 15px 35px;
                align-items: center;
                height: 50px;
            }

            &:nth-child(3) {
                display: flex;
                flex-wrap: wrap;

                &>div {
                    width: 185px;

                    &>span {
                        font-size: 14px;
                    }

                    &>.enable_input {
                        display: none !important;
                    }

                    &>input {
                        height: 28px;
                        width: 100%;
                        text-align: center;
                    }

                    display: flex;
                    gap: 5px;
                    flex-wrap: wrap;
                }


            }

            width: 190px;

        }
    }

    &>div:nth-child(2) {
        &>div:nth-child(1) {
            display: flex;
            flex-wrap: wrap;

            &>div {
                display: flex;
                align-items: center;

                &>span {
                    font-size: 14px;
                }

                &>input {
                    height: 18px;
                }

                &:nth-child(1)>input {
                    width: 100px;
                }

                &:nth-child(2)>input {
                    width: 100px;
                }

                &:nth-child(3)>input {
                    width: 50px;
                }

                &:nth-child(4)>input {
                    width: 50px;
                }
            }
        }

    }
}

.beizhu {
    padding-left: 5px;
    font-size: 10px;
    color: #ff8fab;
}

#addzhishi {
    margin-top: 5px;
    box-sizing: border-box;
    width: 100%;
    height: 45px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #ff8fab;
    border-color: #ff8fab;
    border-radius: 8px;
    border-style: dashed;
    border-width: 1.5;
}
</style>