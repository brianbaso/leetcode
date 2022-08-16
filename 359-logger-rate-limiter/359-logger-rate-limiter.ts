class Logger {
    
    private map
    
    constructor() {
        this.map = new Map()
    }

    shouldPrintMessage(timestamp: number, message: string): boolean {
        if (!this.map.has(message)) {
            this.map.set(message, timestamp)
            return true
        }
        
        else if (timestamp < this.map.get(message) + 10) {
            return false
        }
        
        else {
            this.map.set(message, timestamp)
            return true
        }
    }
}

/**
 * Your Logger object will be instantiated and called as such:
 * var obj = new Logger()
 * var param_1 = obj.shouldPrintMessage(timestamp,message)
 */