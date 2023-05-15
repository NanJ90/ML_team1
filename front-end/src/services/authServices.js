// src/services/authService.js

import axios from 'axios';

export default {
  login(email, password) {
    return axios.post('/api/predict', {
      // email: email,
      password: password
    });
  }
  // Other authentication methods can go here
};
