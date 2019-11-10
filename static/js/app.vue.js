var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        band: {},
        albums: {},
        images: {}
    },
    methods: {
        fetchData: function() {
            this.$http.get('/testband').then(response => {
              this.band = response.body;
            }, response => {
                console.log("an error occurred");
            }).then(() => {
                this.$http.post('/testalbums', {params: {'band': this.band['title']}}).then(response => {
                  this.albums = response.body;
                }, response => {
                    console.log("an error occurred");
                });
              }
            )

            this.$http.get('/getInputImageFilenames').then(response => {
                this.images = response.body;
            })
        }
    },
    mounted: function() {
        this.fetchData();
    }
})