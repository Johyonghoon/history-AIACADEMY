import { context } from "@/components/admin/enums"
import { currentTime } from "@/components/admin/Utils"
import axios, { AxiosResponse } from "axios"

export interface UserType{
    user_id: string
    user_email: string
    password: string
    user_name: string
    phone: string
    birth: string
    address: string
    job: string
    user_interests: string
    token: string
    create_at: string
    updated_at: string
}
export const userSignUpApi = async (payload: {
    user_email: string, 
    password: string,
    phone: string,
    birth: string,
    address: string,
    job: string,
    user_interests: string
}) => {
    const headers = context.headers
    try{
        const response : AxiosResponse<unknown, UserType[]> = await axios.post(`${context.server}`, payload, {headers})
        return response.data
    }catch(err){
        console.log(` ${currentTime} : userSaga 내부에서 SignUp 실패 `)
    }
}
