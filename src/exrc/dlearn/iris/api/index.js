import axios from "axios"
const server = `http://localhost:8000`
export const apiIris = req => axios.post(`${server}/exrc/dlearn/iris`, req)