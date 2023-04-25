<template>
  <LogIn/>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import LogIn from './components/LogIn.vue'
export default {
  name: 'App',
  components: {
    // HelloWorld
    LogIn
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
