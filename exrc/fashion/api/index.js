import axios from "axios"
const server = `http://localhost:8000`
export const fashion = test_num => axios.get(`${server}/exrc/fashion?test_num=${test_num}`)