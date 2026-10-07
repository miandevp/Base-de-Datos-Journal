import csv


class Bucket:

    def __init__(self, capacity):
        self.capacity = capacity
        self.records = []
        self.overflow = None

class Hash:

    def __init__(self,num_buckets, bucket_capacity):
        self.bucket_capacity = bucket_capacity
        self.buckets = []

        for i in range(num_buckets):
            self.buckets.append(Bucket(bucket_capacity))


    def crear_archivo_hash(self,archivo_csv):
        with open(archivo_csv,"r",encoding="utf-8") as archivo:
            lector = csv.reader(archivo)

            next(lector)

            for fila in lector:
                registro = (
                    int(fila[0]),
                    fila[1],
                    int(fila[2])
                )

                self.insert(registro)

    def print(self):

        for bucket in self.buckets:

            bucket_actual = bucket

            while bucket_actual is not None:
            
                for registro in bucket_actual.records: 
                    print(registro)

                bucket_actual = bucket_actual.overflow


    def funcion_hash(self,key):
        return key % len(self.buckets)


    def insert(self,value):
        key = self.funcion_hash(value[0])

        bucket_actual = self.buckets[key]


        while True:
            if (len(bucket_actual.records) < bucket_actual.capacity):
                bucket_actual.records.append(value)
                break

            if bucket_actual.overflow is None:
                    bucket_actual.overflow = Bucket(3)

            bucket_actual = bucket_actual.overflow





    def search(self,key_tupla):

        indice = self.funcion_hash(key_tupla) 

        bucket_actual = self.buckets[indice] 

        while True:

            for registro in bucket_actual.records:
                if registro[0] == key_tupla:
                    return registro

            if bucket_actual.overflow is None:
                break

            bucket_actual = bucket_actual.overflow


        return None



    def delete(self, key_tupla):
        
        indice = self.funcion_hash(key_tupla)

        bucket_actual  = self.buckets[indice]
        bucket_anterior = None

        while bucket_actual is not None:

            for registro in bucket_actual.records:
                if registro[0] == key_tupla:
                    bucket_actual.records.remove(registro)

                    if len(bucket_actual.records) == 0 and bucket_anterior is not None:
                        bucket_anterior.overflow = bucket_actual.overflow


                    return registro

            bucket_anterior = bucket_actual
            bucket_actual = bucket_actual.overflow

        return None

    def update(self, value):

        indice = self.funcion_hash(value[0])

        bucket_actual = self.buckets[indice]

        while True:

            for i in range(len(bucket_actual.records)):
                if bucket_actual.records[i][0] == value[0]:
                    bucket_actual.records[i] = value
                    return value

            if bucket_actual.overflow is None:
                break

            bucket_actual = bucket_actual.overflow

                
        return None