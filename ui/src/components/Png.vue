<template>
    <div id="png">
        <div><img src="" style="width: 125px;" id="logo"></div>
        <div @click="set_png()"><span>更换封面</span></div>
    </div>
</template>
<script setup name="png">
let set_png=async()=>{
    return await pywebview.api.set_png().then(v=>{
        document.querySelector("#logo").src=v;
    });
}
</script>
<style lang="scss">
#png {
    width: 125px;
    height: 140px;
    background-color: #28292e;
    border-radius: 8px;
    border-style: solid;
    border-width: 1px;
    border-color: #a6a6a6;
    display: grid;
    grid-template-rows:100px 30px;
    justify-content: center;
    overflow: hidden;
    &>div:nth-child(2){
        width: 125px;
        display: flex;
        justify-content: center;
        align-items: center ;
        z-index: 999;
        cursor: pointer;
        background-color: rgb(142, 60, 81);
        &>span{
            font-weight: bold;
            font-size: 14px;
        }
    }
}
</style>