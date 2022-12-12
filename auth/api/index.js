import axios from "axios"
const server = `http://localhost:8000`
export const userLogin = req => axios.post(`${server}/blog/blog_users/login`, req)
export const signupApi = req => axios.post(`${server}/blog/auth/signup`, req)