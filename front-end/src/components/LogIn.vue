<template>
   <form @submit.prevent="submitForm">
        <h3>Login</h3>
        <div class="form-group">
            <label>Email</label>
            <input type="text" class="form-control" placeholder="Email" v-model="email"/>
        </div>
        <div class="form-group">
            <label>Password</label>
            <input type="password" class="form-control" placeholder="Password" v-model="password"/>
        </div>

        <button class="'btn btn-primary btn-block'">Login</button>
   </form> 
</template>

<script>
import axios from 'axios';

export default{
  name: 'LogIn',
  data() {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    submitForm() {
      const server = axios.create({
        baseURL: 'http://localhost:5000'
      });
      server.post('/api/predict', {
        email: this.email,
        password: this.password
      })
      .then(response => {
        // handle response here, like redirecting to another page or displaying a success message
        if (response.data.result === 1) {
          alert('The email is potentially malicious!');
        } else {
          alert('The email seems to be good!');
        }
      })
      .catch(error => {
        // handle error here, like displaying an error message
        this.message = `An error occurred: ${error.message}`;
      });
    }
  }
};
</script>