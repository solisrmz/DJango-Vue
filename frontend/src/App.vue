<template>
  <v-app id="app">
    <navigation/>
    <router-view/>
  </v-app>
</template>

<script>
import navigation from "@/components/NavBar"
export default {
  name: 'App', 
  components:{
    navigation
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
