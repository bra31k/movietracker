<template>
    <div id="app">
  <h1>MovieTracker</h1>
  <div v-for="movie in movies" class="movie">
    {{ movie.original_title }}
  </div>
</div>
</template>

<script>
  import axios from 'axios'

export default {
  name: 'HelloWorld',
  data () {
    return {
      movies: 'Welcome to Your Vue.js App'
    }
  },
  created() {
    axios.get('http://localhost:8000/api/v1/movies/?format=json').then(response => (this.movies = response.data));
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
