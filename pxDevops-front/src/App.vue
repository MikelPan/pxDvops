<template>
  <div id="app1">
    <!--<img src="./assets/logo.png">-->
    <h1>{{ title }}</h1>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
  // data () {
  //   return {
  //     title: 'Welcome to Your Vue.js App'
  //   }
  // }
}
</script>

<style>
#app1 {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
h1 {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
