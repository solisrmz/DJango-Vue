<template lang="html">
    <div class="container table-responsive">
    <br/>
        <div class="row">
            <div class="col text-left">
                <h2>Libros disponibles</h2>
                <hr/>
                <div class="col-md-12">
                    <b-table striped hover bordered :items="books" :fields="fields">
                        <template v-slot:cell(actions)="data">
                            <b-button size="sm" variant="primary" :to="{name: 'EditBook', params:{bookId: data.item.id}}">Editar</b-button>
                            <b-button size="sm" @click="delete(data.item)" variant="danger">Eliminar</b-button>
                        </template>
                    </b-table>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
export default {
    data(){
        return{
            fields: [
                {key: 'title', label: 'Titulo'},
                {key: 'resume', label: 'Descripción'},
                {key: 'actions', label:'Acciones'},
            ],
            books: []
        }
    }, 
    created(){
        this.getBooks()
    },
    methods: {
        getBooks(){
            console.log('hola')
            const path = 'http://127.0.0.1:8000/api/v1.0/books/'
            axios.get(path).then((response) => {
                this.books = response.data
            })
            .catch((error)=>{
                console.log('error')
            })
        }, 
        delete(id){
            const path = 'http://127.0.0.1:8000/api/v1.0/books/'+id+'/'
            axios.delete(path).then((response) => {
                swal("Se ha eliminado libro", "", "success")
            })
            .catch((error)=>{
                console.log('error')
            })
        }
    }
}
</script>