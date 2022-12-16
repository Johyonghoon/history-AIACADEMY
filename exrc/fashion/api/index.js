import axios from "axios"
const server = `http://localhost:8000`
export const fashion = test_num => axios(`${server}/exrc/fashion?test_num=${test_num}`)


//export const getfashion = test_num => axios.get(`${server}/exrc/fashion?test_num=${test_num}`)
//export const postfashion = test_num => axios.post(`${server}/exrc/fashion?test_num=${test_num}`, {test_num})
