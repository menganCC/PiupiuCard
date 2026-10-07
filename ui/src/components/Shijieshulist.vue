<template>
    <div id="Shijieshulistbox" @click="$emit('setindex')"
        :class="{ down: props.down.index == props.v ? true : false, Shijieshubiaoqian: down.downindex == props.v ? false : true }">
        <div>
            <span style="white-space: nowrap;overflow: hidden; text-overflow: ellipsis;">{{ jsonall.data.data.character_book.entries[props.v].name }}</span>
            <div @click="$emit('setdownindex')"><svg :class="{ svgdown: down.downindex == props.v ? true : false }"
                    t="1791101299571" class="icon" viewBox="0 0 1024 1024" version="1.1"
                    xmlns="http://www.w3.org/2000/svg" p-id="4883" width="16" height="16">
                    <path d="M0 0h1024v1024H0V0z" fill="#ffffff" opacity=".01" p-id="4884"></path>
                    <path
                        d="M877.4656 317.201067a34.133333 34.133333 0 0 1 0 48.264533l-341.333333 341.333333a34.133333 34.133333 0 0 1-48.264534 0l-341.333333-341.333333a34.133333 34.133333 0 0 1 48.264533-48.264533L512 634.402133l317.201067-317.201066a34.133333 34.133333 0 0 1 48.264533 0z"
                        fill="#ffffff" p-id="4885"></path>
                </svg></div>
        </div>
        <div>
            <div style="--bc:#4b4137;--c:#f39000"
                :class="{ noop: jsonall.data.data.character_book.entries[props.v].constant == true ? false : true }">常驻</div>
            <div style="--bc:#3d3e43;--c:#cccccc"
                :class="{ noop: jsonall.data.data.character_book.entries[props.v].enabled == true ? true : false }">禁用</div>
            <div @click="$emit('delete')" style="--bc:#46454a;cursor: pointer;"><svg t="1791101710209" class="icon" viewBox="0 0 1024 1024" version="1.1"
                    xmlns="http://www.w3.org/2000/svg" p-id="6752" width="25" height="25">
                    <path
                        d="M579.047619 291.352381v-51.2H437.638095v51.2h-170.666666v58.514286h483.961904v-58.514286zM318.171429 831.390476h380.342857V379.12381H318.171429v452.266666z m227.961904-377.904762h64.609524v305.980953h-64.609524V453.485714z m-138.971428 0h64.609524v305.980953h-64.609524V453.485714z"
                        fill="#ff8fab" p-id="6753"></path>
                </svg></div>
        </div>
        <div>
            <div><span>启用条目
                    <Fuxuankuangshijieshulist :v="props.v" :type="true"/>
                </span><span>是否在对话中搜索此关键词</span></div>
            <div><span>常驻条目
                    <Fuxuankuangshijieshulist :v="props.v" />
                </span><span>开启后无需触发词，始终生效</span></div>
            <div>
                <span >条目名称(可选)</span>
                <div><input style="text-align: center;" type="text" v-model="jsonall.data.data.character_book.entries[props.v].name"></div>
            </div>
            <div><span>关键词</span>
                <div>
                    <Shijieshubiaoqian @delete="jsonall.data.data.character_book.entries[props.v].keys.splice(i,1)" v-for="(index, i) in jsonall.data.data.character_book.entries[props.v].keys" :key="i"
                        :v1="props.v" :v2="i" />
                </div>
                <div>
                    <input type="text" v-model="inputvalue" style="text-align: center;">
                    <button @click="jsonall.data.data.character_book.entries[props.v].keys.push(inputvalue)">添加</button>
                </div>
            </div>
            <div><span>元数据</span>
                <div>
                    <div>
                        <span>插入顺序</span>
                        <div><input type="text" v-model="jsonall.data.data.character_book.entries[props.v].insertion_order">
                        </div>
                    </div>
                    <div>
                        <span>优先级</span>
                        <div><input type="text" v-model="jsonall.data.data.character_book.entries[props.v].priority"></div>
                    </div>
                    <div>
                        <span>插入位置</span>
                        <div><input type="text" v-model="jsonall.data.data.character_book.entries[props.v].position"></div>
                    </div>
                </div>
            </div>
            <div>
                <span>注释(可选)</span>
                <div><input type="text" style="text-align: center;" v-model="jsonall.data.data.character_book.entries[props.v].comment"></div>
            </div>
        </div>
    </div>
</template>
<script setup name="shijieshulist">
import { jsonall } from '../main.js';
import Fuxuankuangshijieshulist from './Fuxuankuang_shijieshulist.vue';
import { reactive,ref } from 'vue';
import Shijieshubiaoqian from './Shijieshubiaoqian.vue';
let props = defineProps(["v", "down"]);
const inputvalue=ref("");
</script>
<style lang="scss" scoped>
.noop {
    display: none !important;
}

.down {
    transition: 0.2s;
    border-top-style: solid;
    // box-sizing: border-box;
    border-color: #ff8fab;
    border-width: 2px;
}

.Shijieshubiaoqian {
    transition: 0.2s;
    height: 65px !important;
}

#Shijieshulistbox {
    margin-top: 5px;
    overflow: hidden;
    width: 190px;
    background-color: #3d3239;
    border-radius: 8px;
    height: fit-content;
    padding-bottom: 5px;
    display: grid;
    grid-template-rows: 38px 30px 1fr;

    &>div:nth-child(1) {
        display: grid;
        grid-template-columns: 1fr 20px;
        justify-content: center;
        align-items: center;

        &>span {
            font-weight: bold;
            padding-left: 5px;
        }

        &>div {
            &>svg {
                transform: rotate(-90deg);
            }

            &>.svgdown {
                transform: rotate(0deg);
            }
        }
    }

    &>div:nth-child(2) {
        display: flex;

        &>div {
            width: 40px;
            height: 25px;
            font-size: 12px;
            display: flex;
            margin-left: 5px;
            justify-content: center;
            align-items: center;
            border-radius: 30px;
            background-color: var(--bc);
            color: var(--c);

            &:nth-child(3) {
                width: 30px;
                border-radius: 8px;
                border-style: solid;
                border-color: #9f5c70;
                border-width: 1px;
            }
        }
    }

    &>div:nth-child(3) {
        display: flex;
        flex-wrap: wrap;
        align-content: flex-start;
        gap: 5px;

        &>div:nth-child(1),
        &>div:nth-child(2) {
            width: 100%;
            height: 50px;
            border-radius: 8px;
            background-color: #5f4e59;
            display: grid;
            grid-template-rows: 18px 1fr;
            flex-wrap: wrap;

            &>span {
                display: flex;
                gap: 5px;
                padding: 5px;

                &:nth-child(1) {
                    font-size: 14px;
                    font-weight: bold;
                }

                &:nth-child(2) {
                    color: #ff8fab;
                    font-size: 10px;
                    align-self: center;
                }
            }

        }

        &>div:nth-child(3) {
            display: grid;
            width: 185px;
            grid-template-rows: 25px 30px;

            &>span {
                font-size: 12px;
            }

            &>div>input {
                width: 100%;
                height: 30px;
            }
        }

        &>div:nth-child(4) {
            width: 185px;

            &>span {
                font-size: 12px;
            }

            &>div {
                display: flex;
                flex-wrap: wrap;
                gap: 5px;

                &>input {
                    margin-top: 5px;
                    width: 100%;
                    height: 30px;
                }

                &>button {
                    width: 100%;

                }
            }
        }

        &>div:nth-child(5) {
            &>span {
                font-size: 12px;
            }

            display: grid;
            grid-template-rows:25px 60px;

            &>div {
                display: grid;
                grid-template-columns: repeat(3, 1fr);

                &>div {
                    display: grid;
                    grid-template-rows: 25px 1fr;
                    justify-content: center;

                    &>span {
                        font-size: 12px;
                    }

                    &>div>input {
                        text-align: center;
                        width: 60px;
                        height: 30px;
                    }
                }
            }
        }

        &>div:nth-child(6) {
            display: grid;
            width: 185px;
            grid-template-rows: 25px 1fr;

            &>span {
                font-size: 12px;
            }

            &>div>input {
                width: 100%;
                height: 30px;
            }
        }
    }
}
</style>