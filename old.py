 #for addr in r:
                #n_unspent = self.btc.unspent(addr[0])
                #if len(n_unspent) != 0:
                    #all_in.extend(n_unspent)
                    #priv_all_in[addr[0]] = addr[1]

            #for unsp in all_in:
                #if inputs_summ <= summ:
                    #inputs.append(unsp)
                    #addr = unsp['address']
                    #priv_key = priv_all_in.get(addr)
                    #priv[addr] = priv_key
                    #inputs_summ += unsp['value']
            #for addr in r:
                #if inputs_summ < summ:
                    #t1 = time.time()
                    #new_unspent = self.btc.unspent(addr[0])
                    #s += time.time()-t1
                    #print(new_unspent)
                    #if len(new_unspent) != 0:
                        #for inp in new_unspent:
                        #inputs.extend(new_unspent)
                        #priv[addr[0]] = addr[1]
                        #inputs_summ = sum(i['value'] for i in inputs)
                        
     # Функция добавления ключей в БД
    def add_keys_to_db(self, public_key, addr):
        db = sqlcipher3.connect(__db_path__)
        cur = db.cursor()
        r = cur.execute('select * from keys where public_key = ?',(public_key,))
        if r.fetchone() is None:
            cur.execute('INSERT INTO keys (public_key, address) VALUES (?, ?)',(str(public_key), str(addr)))
        #cur.execute('INSERT INTO mnemonic_public_key (xpub_key) VALUES (?)',(xpub_key))
        db.commit()
