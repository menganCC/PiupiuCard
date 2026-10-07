<template>
    <div id="Shijieshubiaoqian">
        <span>{{ jsonall.data.data.character_book.entries[v1].keys[v2] }}</span>
        <div @click="$emit('delete')"><svg t="1791106670245" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="7699" width="16" height="16"><path d="M763.392 818.176c0 29.44-23.872 54.72-54.784 54.72H315.392a54.848 54.848 0 0 1-54.784-54.72V239.552h502.784v578.56zM368.768 141.248c0-2.816 1.408-5.632 2.816-8.448 1.408-1.408 4.16-2.816 8.384-2.816h262.656c5.632 0 11.2 4.224 11.2 11.264v32.32H368.768v-32.32z m558.912 32.32h-207.808v-32.32C719.872 99.136 686.08 64 642.56 64H379.968C337.92 64 302.72 97.728 302.72 141.248v32.32H96.32a30.912 30.912 0 0 0-28.16 16.832 33.088 33.088 0 0 0 28.16 49.152H194.56v580.032c0 65.984 53.376 120.768 120.768 120.768h393.216a120.768 120.768 0 0 0 120.768-120.768V239.552h98.304c18.304 0 32.32-14.08 32.32-32.32 0-18.24-15.424-33.664-32.32-33.664zM512 774.592c18.24 0 32.32-14.016 32.32-32.256V392.64a30.912 30.912 0 0 0-16.896-28.16 33.088 33.088 0 0 0-49.152 28.16v349.696c0 18.24 15.488 32.256 33.728 32.256z m-153.088 0a32.896 32.896 0 0 0 23.872-9.792 33.92 33.92 0 0 0 9.856-23.872V392.64a30.912 30.912 0 0 0-16.896-28.16 33.088 33.088 0 0 0-49.152 28.16v349.696c-1.344 18.24 14.08 32.256 32.32 32.256z m306.176 0c18.24 0 32.32-14.016 32.32-32.256V392.64a30.912 30.912 0 0 0-16.896-28.16 33.088 33.088 0 0 0-49.152 28.16v349.696c0 18.24 15.488 32.256 33.728 32.256z" fill="#FFFFFF" p-id="7700"></path></svg></div>
    </div>
</template>
<script setup name="shijieshubiaoqian">
import { jsonall } from '../main';
let props=defineProps(['v1','v2']);
</script>
<style lang="scss" scoped>
#Shijieshubiaoqian {
    max-width: 180px;
    width: fit-content;
    height: 25px;
    display: flex;
    justify-content: center;
    align-items: center;
    padding-left: 5px;
    padding-right: 3px;
    border-radius: 8px;
    background-color: #ff8fab;
    &>span{
        text-overflow: ellipsis;
        overflow: hidden;
        white-space: nowrap;
        padding-bottom: 3px;
        font-size: 14px;
    }
    &>div{
        padding-left: 5px;
    }
}
</style>