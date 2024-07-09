import semchunk

def get_topic_segments(transcript, tokens_per_chunk=100):
    chunker = semchunk.chunkerify(lambda text: len(text.split()), chunk_size=tokens_per_chunk)
    chunks = chunker(transcript)
    return chunks