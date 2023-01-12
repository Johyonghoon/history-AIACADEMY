import axios, { AxiosResponse } from 'axios'
import { context } from '@/components/admin/enums'
import { UserType } from '@/apis/userApi'
import { currentTime } from '@/components/admin/Utils'


export const signUpApi = async (payload: {
    user_email: string, 
    password: string, 
    user_name: string, 
    phone: string, 
    birth: string, 
    address: string, 
    job: string, 
    user_interests: string
}) => {
    try{
        const response : AxiosResponse<unknown, UserType[]> = await axios.post(`${context.server}/users`)
        return response.data
    }catch(err){
        console.log(` ${currentTime} : userSaga 내부에서 join 실패 `)
    }
}
