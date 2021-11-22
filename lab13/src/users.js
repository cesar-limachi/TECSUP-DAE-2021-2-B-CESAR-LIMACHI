import React from 'react'
import { useParams } from "react-router-dom";

const Users = () =>{
            let params = useParams();
            return (
            <div>
                <h1>Usuarios</h1>
                <p>{params.id}</p>
            </div>)

    }

export default Users;
