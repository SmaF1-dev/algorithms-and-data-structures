from lab1.task5.src.main import main
import tracemalloc

tracemalloc.start()

main()

print("Максимально занимаемая память: "+str(tracemalloc.get_traced_memory()[1]/1024)+" KB")
tracemalloc.stop()