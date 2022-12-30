import 'exrc/auth/users/styles/UserList.css'

import axios from "axios"
import { useState } from "react"
import { useEffect } from "react"
import ListForm from '../components/ListForm'

export default function UserList(){
    const [list, setList] = useState([])
    useEffect(()=> {
        fetchList()
    }, [])
    const fetchList = () => {
        axios
        .get('http://127.0.0.1:8000/exrc/auth/user-list')
        .then(res => {setList(res.data)})
        .catch(err =>{console.log(err)})
    }
    return <><ListForm list={list}/></>
}