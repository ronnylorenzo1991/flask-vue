import dayjs from 'dayjs'

export function nativeGet(obj, path, defaultValue = undefined) {
    const travel = regexp =>
        String.prototype.split
            .call(path, regexp)
            .filter(Boolean)
            .reduce((res, key) => (res !== null && res !== undefined ? res[key] : res), obj)
    const result = travel(/[,[\]]+?/) || travel(/[,[\].]+?/)
    return result === undefined || result === obj ? defaultValue : result
}

export function formatDate(date){
    if (!date) {
        return ''
    }
    
    return dayjs(date).format('DD-MM-YYYY')
}

export default {
    nativeGet,
    formatDate
}