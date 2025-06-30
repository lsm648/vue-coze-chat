<template>
    <div id="app">
        <RouterView></RouterView>
    </div>
</template>

<script setup>
import Home from './view/Home.vue';

console.log("hi~")

</script>

<style>
* {
    padding: 0;
    margin: 0;
}

#app {
    width: 100vw;
    height: 100vh;
    background-color: rgb(128, 133, 141);
    display: flex;
    align-items: center;
}
</style>