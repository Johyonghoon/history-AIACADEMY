import os

import pandas as pd
import torch
from torch.utils.data import DataLoader
from transformers import GPT2LMHeadModel

from app.admin.path import dir_path
from app.trains.skt_gpt2_dataset import collate_batch, ChatbotDataset


class SKTModel:

    def modeling(self):

        model = GPT2LMHeadModel.from_pretrained('skt/kogpt2-base-v2')

        chatbot_data = pd.read_csv(os.path.join(dir_path("trains"), "data", "skt", "skt_chatbot_data.csv"))
        # Test 용으로 300개 데이터만 처리한다.
        chatbot_data = chatbot_data[:300]
        chatbot_data.head()

        device = torch.device("cpu")
        train_set = ChatbotDataset(chatbot_data, max_len=40)
        # 윈도우 환경에서 num_workers 는 무조건 0으로 지정, 리눅스에서는 2
        train_dataloader = DataLoader(train_set, batch_size=32, num_workers=0, shuffle=True, collate_fn=collate_batch,)

        model.to(device)
        model.train()

        learning_rate = 3e-5
        criterion = torch.nn.CrossEntropyLoss(reduction="none")
        optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

        epoch = 10
        sneg = -1e18

        print("start")
        i = 0
        for epoch in range(epoch):
            i += 1
            print(f"{i}번째 epoch")
            for batch_idx, samples in enumerate(train_dataloader):
                optimizer.zero_grad()
                token_ids, mask, label = samples
                out = model(token_ids)
                out = out.logits      # Returns a new tensor with the logit of the elements of input
                mask_3d = mask.unsqueeze(dim=2).repeat_interleave(repeats=out.shape[2], dim=2)
                mask_out = torch.where(mask_3d == 1, out, sneg * torch.ones_like(out))
                loss = criterion(mask_out.transpose(2, 1), label)
                # 평균 loss 만들기 avg_loss[0] / avg_loss[1] <- loss 정규화
                avg_loss = loss.sum() / mask.sum()
                avg_loss.backward()
                # 학습 끝
                optimizer.step()
        print("end")

        torch.save(model, os.path.join(dir_path("models"), "chatbot", "../models/chatbot/skt_model.pt"))
        # torch.save(model.state_dict(), os.path.join(dir_path("models"), "chatbot", "skt_model.pt"))


if __name__ == '__main__':
    SKTChatbot().modeling()
