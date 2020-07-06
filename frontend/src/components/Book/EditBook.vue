<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Editar un libro</h2>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <div class="card">
                    <div class="card-header">Editar</div>
                    <div class="card-body">
                        <form @submit="onSubmit"> 
                            <div class="form-group row">
                                <label for="title" class="col-sm-2 col-form-label">Título</label>
                                <div class="col-sm-6">
                                    <input type="text" class="form-control" name="title" placeholder="Titulo" v-model.trim="form.title">
                                </div>
                            </div>
                            <div class="form-group row">
                                <label for="resume" class="col-sm-2 col-form-label">Título</label>
                                <div class="col-sm-6">
                                    <textarea type="text" name="resume" class="form-control" placeholder="Descripción" rows="3" v-model.trim="form.resume"></textarea>
                                </div>
                            </div>
                            <div class="rows">
                                <div class="col text-left">
                                    <b-button type="submit" variant="primary">Editar</b-button>
                                    <b-button type="submit" variant="secondary" class="btn-large-space" :to="{name: 'ListBook'}">Cancelar</b-button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
    export default{
        data(){
            return {
                bookId: this.$route.params.bookId,
                form: {
                    title: '',
                    resume: ''
                }
            }
        },
        created(){
            console.log(this.$route.params.bookId);
            this.bookId = this.$route.params.bookId;
            this.getBook()
        },
        methods:{
            onSubmit(evt){
                evt.preventDefault()
                const path = 'http://127.0.0.1:8000/api/v1.0/books/'+this.bookId+'/'
                axios.put(path, this.form).then((response) => {
                    this.form.title = response.data.title
                    this.form.resume = response.data.resume
                    alert('Libro actualizado')
                })
                .catch((error)=>{
                    console.log('error')
                })
            },
            getBook(){
                const path = 'http://127.0.0.1:8000/api/v1.0/books/'+this.bookId+'/'
                axios.get(path).then((response) => {
                    this.form.title = response.data.title
                    this.form.resume = response.data.resume
                })
                .catch((error)=>{
                    console.log('error')
                })
            }
        }
    }
</script>