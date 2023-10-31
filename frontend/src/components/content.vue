<template>
    <div id="page" class="content exportedElement" contenteditable="false" :data-attr="dataAttr"
        :style="{ color, '--font-size': fontSize, '--top': top, '--bg-color': bgColor, '--borader-color': borderColor }">
        <slot name="content">
            <h1>占位</h1>
        </slot>
    </div>
</template>
<script setup>
const props = defineProps({
    dataAttr: {
        type: String,
        default: '',
    },
    color: {
        type: String,
    },
    fontSize: {
        type: String,
    },
    top: {
        type: String,
    },
    bgColor: {
        type: String,
        default: '#F17C72',
    },
    borderColor: {
        type: String,
        default: '#334960',
    }
});
</script>
<style>
.exportedElement {
    display: flex;
    justify-content: center;
    background-color: var(--bg-color);
    border-width: 0;
    color: #ECEDEF;
    height: max-content;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 100%;
    line-height: 19px;
    margin: 0 0;
    outline: 0;
    padding: 100px 0 30px 0;
    position: relative;
    text-align: left;
    text-size-adjust: none;
    vertical-align: top;
    font-size: var(--font-size);
}

.exportedElement::before {
    position: absolute;
    content: attr(data-attr);
    top: var(--top);
    z-index: 3;
}

.exportedElement::after {
    border-color: var(--borader-color) transparent transparent;
    border-style: solid;
    border-width: 50px 80px;
    content: "";

    display: flex;
    height: 0;
    left: 35%;
    margin: 0;
    position: absolute;
    top: 0;
    width: 30%;
    z-index: 1;
}

@media only screen and (min-width: 768px) and (max-width: 959px) {
    .exportedElement>div {
        width: 768px;
    }
}

@media only screen and (max-width: 767px) {
    .exportedElement>div {
        width: 100%;
    }
}

@media only screen and (min-width: 620px) and (max-width: 767px) {
    .exportedElement>div {
        width: 100%;
    }
}

@media only screen and (max-width: 619px) {
    .exportedElement>div {
        width: 100%;
    }
}
</style>