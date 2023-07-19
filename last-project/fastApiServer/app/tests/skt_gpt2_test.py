import os

import torch
from transformers import PreTrainedTokenizerFast

from app.admin.path import dir_path


class SKTGpt2Test:
    def process(self):
        Q_TKN = "<usr>"
        A_TKN = "<sys>"
        BOS = '</s>'
        EOS = '</s>'
        MASK = '<unused0>'
        SENT = '<unused1>'
        PAD = '<pad>'
        koGPT2_TOKENIZER = PreTrainedTokenizerFast.from_pretrained("skt/kogpt2-base-v2",
                                                                   bos_token=BOS, eos_token=EOS, unk_token='<unk>',
                                                                   pad_token=PAD, mask_token=MASK)

        model = torch.load(os.path.join(dir_path("models"), "chatbot", "skt_model.pt"), map_location='cpu')
        with torch.no_grad():
            while 1:
                q = input("user > ").strip()
                if q == "quit":
                    break
                a = ""
                while 1:
                    input_ids = torch.LongTensor(
                        koGPT2_TOKENIZER.encode(Q_TKN + q + SENT + '0' + A_TKN + a)).unsqueeze(dim=0)
                    pred = model(input_ids)
                    pred = pred.logits
                    gen = koGPT2_TOKENIZER.convert_ids_to_tokens(
                        torch.argmax(pred, dim=-1).squeeze().numpy().tolist())[-1]
                    if gen == EOS:
                        break
                    a += gen.replace("▁", " ")
                print("Chatbot > {}".format(a.strip()))


if __name__ == '__main__':
    SKTGpt2Test().process()
