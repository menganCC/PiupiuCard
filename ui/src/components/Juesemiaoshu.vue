<template>
    <div id="juesemiaoshubox">
        <monaco :options="{
            wordWrap: 'on',
            automaticLayout:true
        }" v-model:value="jsonall.data.data.description" style="border-radius: 8px;overflow: hidden;"
            theme="vs-dark" language="text" />
    </div>
</template>
<script setup name="juesemiaoshu">
import monaco from "monaco-editor-vue3"
import { jsonall } from "../main";
</script>
<style lang="scss" scoped>
#juesemiaoshubox {
    overflow: hidden;
    width: 100%;
    height: 100%;
}
</style>