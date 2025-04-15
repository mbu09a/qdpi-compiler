# QDPI Compiler v0.1 – Engine Bootstrap
from reader import read_input
from parser import parse_input
from indexer import retrieve_fragments
from transformer import transform
from emitter import emit
from memory import update_memory

def run_qdpi_cycle(user_input):
    parsed = parse_input(read_input(user_input))
    indexed = retrieve_fragments(parsed)
    output = transform(indexed)
    emit(output)
    update_memory(user_input, output)

if __name__ == "__main__":
    user_text = input("Gift something to the Compiler: ")
    run_qdpi_cycle(user_text)
