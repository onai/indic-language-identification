from fasttext import load_model
import sys

model = load_model(sys.argv[1])
train_f = sys.argv[2]

model.quantize(input=train_f, retrain=True)
#print_results(*model.test(valid_data))

model.save_model(sys.argv[1].replace('bin', 'ftz'))