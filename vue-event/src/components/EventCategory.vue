<template>
  <div class="home">
    <h1>Це головна сторінка по організації подій</h1>
  </div>
</template>

<script>
export default {
  name: 'EventCategory',
  date(){
    return{
        listCategory: []
    }
  },
  components: {}
  created(){
  },
  methods: {
    async loadListEvent(){
        this.listCategory = await fetch(
            input: '${this.$store.getters.getServerUrl}/api_event/category'
        ).then(response => response.json())
        console.log(this.listCategory)
    }
  }
}
</script>

<style scoped>
    .home {
        text-align: center;
    }
    h1{
        color: red;
    }
</style>