<script setup name="Head">
import { jsonall } from '../main';
import { 保存状态 } from '../main';
let props = defineProps(['sx']);
let get_png = async () => {
    return pywebview.api.get_png().then(v => {
        jsonall.data = JSON.parse(v[1]);
        document.querySelector("#logo").src = v[0];
    });
}
let get_json = async () => {
    return pywebview.api.get_json();
}
let save_file = async (x) => {
    // 1=正在保存
    // 2=保存成功
    // 3=保存失败
    保存状态.value=1
    let a=await pywebview.api.save_file(JSON.stringify(x))
    return a;
}
let 还原=async()=>{
    setInterval(() => {
            保存状态.value=-1;
        }, 1000);
}

</script>

<template>
    <div id="box">
        <button @click="get_png()">导入png</button>
        <button @click="get_json().then(v => { if (v != null) { jsonall.data = JSON.parse(v) } })">导入json</button>
        <input type="text" placeholder="名称" v-model="jsonall.data.data.name" id="projectname">
        <button @click="save_file(jsonall.data).then(x=>{保存状态=x;还原()})">导出</button>
    </div>
</template>

<style scoped lang="scss">
#box {
    width: 100vw;
    height: v-bind("props.sx.h + 'px'");
    display: grid;
    grid-template-columns: 80px 80px 1fr 80px;
    grid-template-rows: 100%;
    background: linear-gradient(0deg, #3b2732 -5%, #1c1d22 50%);
    justify-content: center;
    align-items: center;
    gap: 2px;

    button {
        font-weight: bold;
        margin: 2px;
        height: v-bind("props.sx.h - 15 + 'px'");
        width: 75px;
        border-radius: 10px;
    }

    input {
        font-size: 20px;
        height: v-bind("props.sx.h - 15 + 'px'");
        text-align: center;
        font-weight: bold;
        border-width: 1px;
        border-color: #544d55;
    }
}
</style>