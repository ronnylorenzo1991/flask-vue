import Swal from 'sweetalert2'
import { nativeGet } from './helpers'

export async function error(message, errors = null) {
    return Swal.fire({
        icon: 'error',
        confirmButtonText: 'Aceptar',
        confirmButtonColor: '3C50E0',
        title: message,
        text: errors ? getErrors(errors) : 'Lo sentimos. Parece que algo anda mal.',
    })
}

export async function success(message) {
    return Swal.fire({
        icon: 'success',
        confirmButtonText: 'Aceptar',
        confirmButtonColor: '3C50E0',
        title: 'Correcto',
        text: message ? message : 'Ejecución Satisfactoria',
    })
}

export function confirm(title, icon = 'warning', showCancelButton = true, confirmButtonColor = '#3C50E0', cancelButtonColor = '#AEB7C0', confirmButtonText = 'Aceptar', cancelButtonText = 'Cancelar') {
    return new Promise((resolve) => {
        Swal.fire({
            icon: icon,
            title: title,
            showCancelButton: showCancelButton,
            confirmButtonText: confirmButtonText,
            cancelButtonText: cancelButtonText,
            confirmButtonColor: confirmButtonColor,
            cancelButtonColor: cancelButtonColor,
        }).then(response => {
            if (nativeGet(response, 'dismiss') === 'close') {
                resolve('close')
            }
            resolve(nativeGet(response, 'value') === true)
        }).catch(() => {
            resolve(false)
        })
    })
}

function getErrors(errors) {
    let str = ''
    Object.keys(errors).forEach((item) => {
        str += errors[item] + '<br>'
    })

    return str
}

export default {
    error,
    success,
    confirm,
}
