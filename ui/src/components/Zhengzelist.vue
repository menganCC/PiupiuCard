<template>
    <div id="zhengzelistbox" @click="$emit('setindex')" :class="{zdown:props.index.index==props.v?true:false}">
        <div>
            <span>
                {{ jsonall.data.data.extensions.piupiu_regex.scripts[props.v].scriptName }}
            </span>
            <Fuxuankuang_zhengze_list :v="props.v"/>
        </div>
        <div>
            <div>
                <div :class="{enable:jsonall.data.data.extensions.piupiu_regex.scripts[props.v].disabled}">启用</div>
                <div @click="$emit('delete')"><svg t="1791189630824" class="icon" viewBox="0 0 1024 1024" version="1.1"
                        xmlns="http://www.w3.org/2000/svg" p-id="6022" width="16" height="16">
                        <path
                            d="M781.28 851.36a58.56 58.56 0 0 1-58.56 58.56H301.28a58.72 58.72 0 0 1-58.56-58.56V230.4h538.56z m-421.6-725.92a11.84 11.84 0 0 1 12-12h281.28a11.84 11.84 0 0 1 12 12V160H359.68zM956.8 160H734.72v-34.56a81.76 81.76 0 0 0-81.76-81.76H371.68a82.08 82.08 0 0 0-81.76 81.76V160H67.2a35.36 35.36 0 0 0 0 70.56h105.12v620.8a128.96 128.96 0 0 0 128.96 128.96h421.44a128.96 128.96 0 0 0 128.96-128.96V230.4H956.8a35.2 35.2 0 0 0 35.2-35.2 34.56 34.56 0 0 0-35.2-35.2zM512 804.16a35.2 35.2 0 0 0 35.2-35.36V393.92a35.2 35.2 0 1 0-70.4 0V768.8a35.2 35.2 0 0 0 35.2 35.36m-164.32 0a35.36 35.36 0 0 0 35.36-35.36V393.92a35.36 35.36 0 1 0-70.56 0V768.8a36.32 36.32 0 0 0 35.2 35.36m328.64 0a35.36 35.36 0 0 0 35.2-35.36V393.92a35.36 35.36 0 1 0-70.56 0V768.8a35.36 35.36 0 0 0 35.36 35.36"
                            fill="#ff8fab" p-id="6023"></path>
                    </svg></div>
            </div>
            <div>
                <div>脚本名称</div>
                <div><input type="text" v-model="jsonall.data.data.extensions.piupiu_regex.scripts[props.v].scriptName"></div>
            </div>
        </div>
        <!-- {{ props.v }} -->
    </div>
</template>
<script setup name="zhengzelist">
import { jsonall } from '../main';
import Fuxuankuang_zhengze_list from './Fuxuankuang_zhengze_list.vue';
let props = defineProps(["v","index"]);
</script>
<style lang="scss" scoped>
.enable{
    display: none !important;
}
.zdown{
    border-style: dashed;
    box-sizing: border-box;
    border-color: #ff8fab;
}
#zhengzelistbox {
    overflow: hidden;
    background-color: #3d3239;
    width: 185px;
    border-radius: 8px;
    // height: 80px;
    height: fit-content;
    display: grid;
    grid-template-rows: 30px 1fr;

    &>div:nth-child(1) {
        display: grid;
        align-items: center;
        grid-template-columns: 1fr 32px;

        &>span {
            overflow: hidden;
            padding-left: 8px;
            font-size: 14px;
            font-weight: bold;
            text-overflow: ellipsis;
            text-wrap-mode: nowrap;
        }

        &>div {
            justify-self: center;
        }
    }

    &>div:nth-child(2) {
        &>div:nth-child(1) {
            padding-left: 8px;

            &>div:nth-child(1) {
                width: 40px;
                height: 20px;
                font-size: 12px;
                display: flex;
                justify-content: center;
                align-items: center;
                color: #537d42;
                background-color: #ddfcd4;
                border-radius: 30px;
                font-weight: bold;
            }

            &>div:nth-child(2) {
                width: 20px;
                height: 20px;
                display: flex;
                justify-content: center;
                align-items: center;
                border-radius: 8px;
                background-color: #46454a;
            }

            gap: 5px;
            display: flex;
        }

        &>div:nth-child(2) {
            &>div {
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                font-size: 14px;
                &>input{
                    width: 170px;
                    text-align: center;
                    height: 30px;
                }
            }
            padding-bottom: 10px;
        }
    }
}
</style>