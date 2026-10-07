<template>
    <div @click="$emit('setindex')" id="beixuanlist" :class="{beixuanup:props.down.id==props.i?true:false}">
        <span>
            {{ props.data }}
        </span>
        <div @click="$emit('delete')">
            <svg t="1791037760075" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                p-id="10145" width="16" height="16">
                <path
                    d="M781.28 851.36a58.56 58.56 0 0 1-58.56 58.56H301.28a58.72 58.72 0 0 1-58.56-58.56V230.4h538.56zM359.68 125.44a11.84 11.84 0 0 1 12-12h281.28a11.84 11.84 0 0 1 12 12V160H359.68zM956.8 160H734.72V125.44a81.76 81.76 0 0 0-81.76-81.76H371.68a82.08 82.08 0 0 0-81.76 81.76V160H67.2a35.36 35.36 0 0 0 0 70.56h105.12v620.8a128.96 128.96 0 0 0 128.96 128.96h421.44a128.96 128.96 0 0 0 128.96-128.96V230.4h105.12a35.2 35.2 0 0 0 35.2-35.2 34.56 34.56 0 0 0-35.2-35.2zM512 804.16a35.2 35.2 0 0 0 35.2-35.36V393.92a35.2 35.2 0 1 0-70.4 0v374.88a35.2 35.2 0 0 0 35.2 35.36m-164.32 0a35.36 35.36 0 0 0 35.36-35.36V393.92a35.36 35.36 0 1 0-70.56 0v374.88a36.32 36.32 0 0 0 35.2 35.36m328.64 0a35.36 35.36 0 0 0 35.2-35.36V393.92a35.36 35.36 0 1 0-70.56 0v374.88a35.36 35.36 0 0 0 35.36 35.36"
                    fill="#d81e06" p-id="10146"></path>
            </svg>
        </div>
    </div>
</template>
<script setup name="beixuanlist">
let props = defineProps(["data","down","i"]);
</script>
<style lang="scss">
#beixuanlist {
    &>div{
        &:hover{
            &>svg>path{
                fill:white;
            }
        }
    }
    display: grid;
    grid-template-columns: 100px 40px;
    align-items: center;
    cursor: pointer;
    width: 130px;
    height: 35px;
    border-radius: 8px;
    background-color: #3d3239;
    &:hover{
        &>div>svg>path{
            fill: #ffffff;
        }
        box-sizing: border-box;
        border-style: dashed;
    }

    span {
        text-overflow: ellipsis;
        overflow: hidden;
        white-space: nowrap;
        padding-left: 5px;
        font-size: 14px;
    }
}
.beixuanup{
    border-style: dashed !important;
    border-color:#ff8fab !important;
    box-sizing: border-box !important;
}
</style>