import axios from "axios"
const server = `http://localhost:8000`
export const stroke = req => axios.get(`${server}/exrc/stroke`, req)
export const iris = req => axios.post(`${server}/exrc/iris`, req)