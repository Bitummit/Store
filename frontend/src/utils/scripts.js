function setHeaders() {
    let headers = {
        'Content-Type': 'application/json'
      }
      if (this.$store.state.isAuth) {
        headers['Authorization'] = 'Token' + this.$store.state.token
      }
      return headers
}
