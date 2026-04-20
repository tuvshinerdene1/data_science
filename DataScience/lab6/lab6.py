############################
######### Дасгал 1 #########
############################
def pairwise_div(Lnum, Ldenom):
    """Lnum болон Ldenom нь тоо агуулсан, ижил урттай,
        хоосон биш жагсаалт
    Хоёр жагсаалтыг харгалзах элемент бүрээр хувааж, хариуг
    агуулсан шинэ жагсаалт буцаана (Lnum/Ldenom).
    Хэрэв Ldenom жагсаалт 0 утга агуулсан эсвэл ямар нэг байдлаар
    хуваахад асуудал гарсан тохиолдолд ValueError алдаа үүсгэ."""
    # Энд кодоо бичнэ үү...
    # if len(Lnum) != len(Ldenom):
    #     raise AssertionError("Хүснэгтүүдийн хэмжээ өөр")
    assert len(Lnum) != len(Ldenom), "Хүснэгтүүдийн хэмжээ өөр"
    try:
        result = [ a / b for a , b in zip(Lnum, Ldenom)]
        return result
    except ZeroDivisionError:
        raise ValueError("Ldenom dotor 0 baina")
    except Exception:
        raise ValueError("Aldaa garlaa")
    



# Жишээ:
# L1 = [5, 10, 15, 20]
# L2 = [1, 3, 4, 2]
# print(pairwise_div(L1, L2))  # prints [5.0, 3.3333, 3.75, 10]

# L1 = [5, 10, 15, 20]
# L2 = [5, 4, 3]
# print(pairwise_div(L1, L2))  # raises AssertionError

# L1 = []
# L2 = [5, 4, 3, 2]
# print(pairwise_div([], [5, 4, 3, 2]))  # raises AssertionError

# L1 = [5, 10, 15, 20]
# L2 = [1, 3, 0, 2]
# print(pairwise_div(L1, L2))  # raises ValueError


############################
######### Дасгал 2 #########
############################
def sum_str_lengths(L):
    """
    L нь хоосон биш жагсаалт бөгөөд дараах өгөгдлийн төрлүүдийг агуулна:
    * тэмдэгт мөрүүд эсвэл
    * тэмдэгт мөр агуулсан хоосон биш дэд жагсаалт
    L жагсаалт доторх бүх тэмдэгт мөр, мөн дэд жагсаалт байвал
    түүн доторх тэмдэгт мөр бүрийн уртыг олж,
    нийлбэрийг буцаана. Хэрэв L жагсаалтад тэмдэгт мөрөөс
    өөр төрөлтэй өгөгдөл олдох юм бол ValueError алдаа үүсгэнэ үү.
    """
    # Энд кодоо бичнэ үү...
    result = 0
    for x in L:
        if type(x) == str:
            result += len(x)
        elif isinstance(x, list):
            result += sum_str_lengths(x)  # ValueError will naturally bubble up
        else:
            raise ValueError(f"Unexpected type: {type(x)}")
    return result

            


# Жишээ:


if __name__ == "__main__":
    test_cases = [
        lambda: print(pairwise_div([5,10,15,20], [1,3,4,2])),   
        lambda: print(pairwise_div([5,10,15,20], [5,4,3])),    
        lambda: print(pairwise_div([], [5,4,3,2])),           
        lambda: print(pairwise_div([5,10,15,20], [1,3,0,2])),  

        lambda: print(sum_str_lengths(["abcd", ["e", "fg"]])), 
        lambda: print(sum_str_lengths([12, ["e", "fg"]])),     
        lambda: print(sum_str_lengths(["abcd", [3, "fg"]])),  
    ]

    for test in test_cases:
        try:
            test()
        except (AssertionError, ValueError) as e:
            print(f"Caught expected error: {type(e).__name__}: {e}")