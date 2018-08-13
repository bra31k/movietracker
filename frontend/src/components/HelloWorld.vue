<template>
  <div id="app">
    <div class="container">
      <div class="row">
        <div v-for="movie in movies" class="movie">
          <div class="col-sm">
          <b-card v-bind:title="movie.original_title"
                  v-bind:img-src="'https://image.tmdb.org/t/p/w370_and_h556_bestv2/' + movie.poster_path"
                  img-alt="Image"
                  img-bot
                  tag="article"
                  style="max-width: 12rem;"
                  class="mb-3">
            <p class="card-text">
            </p>
            <button type="button" class="btn btn-info">Info</button>
          </b-card>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
  import axios from 'axios'
  import 'bootstrap/dist/css/bootstrap.css'
  import 'bootstrap-vue/dist/bootstrap-vue.css'

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
body {
   background-color: #000000;
}
</style>
