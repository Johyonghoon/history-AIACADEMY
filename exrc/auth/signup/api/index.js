import axios from "axios"
const server = `http://localhost:8000`
export const apiSignUp = req => axios.post(`${server}/exrc/auth/signup`, req)