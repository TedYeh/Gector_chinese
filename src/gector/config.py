class Args:
    bert_dir = "hfl/chinese-macbert-large"
    output_dir = "./checkpoints/"
    ctc_vocab_dir = "./data/ctc_vocab/"
    detect_tags_file = "ctc_detect_tags.txt"
    log_dir = "./logs/"

    data_name = "wang"
    model_name = "macbert_large"
    correct_tags_file = "ctc_correct_tags.txt"

    warmup_proportion = 0.01
    learning_rate = 3e-5
    adam_epsilon = 1e-8
    seed = 999
    max_seq_len = 128
    use_tensorboard = False
    batch_size = 128
    epochs = 10
    eval_step = 5000
    max_grad_norm = 1.0

    detect_vocab_size = 2
    correct_vocab_size = 20675

    # nlpcc
    nlpcc_train_path = "./data/nlpcc/train.json"
    nlpcc_dev_path = "./data/nlpcc/dev.json"
    nlpcc_test_path = "./data/nlpcc/CGED20_testdata_nsp.json"
    nlpcc_detect_tags_path = "ctc_detect_tags.txt"
    nlpcc_correct_tags_path = "ctc_correct_tags.txt"

    # nlpcc_sw
    nlpcc_sw_train_path = "./data/nlpcc_sw/train.json"
    nlpcc_sw_dev_path = "./data/nlpcc_sw/dev.json"
    nlpcc_sw_test_path = "./data/nlpcc/CGED20_testdata_nsp.json"
    nlpcc_sw_detect_tags_path = "ctc_detect_tags.txt"
    nlpcc_sw_correct_tags_path = "ctc_correct_tags.txt"

    # wang
    wang_train_path = "./data/wang/train.json"
    wang_dev_path = "./data/wang/dev.json"
    wang_test_path = "./data/wang/test.json"
    wang_detect_tags_path = "ctc_detect_tags.txt"
    wang_correct_tags_path = "ctc_correct_wang_tags.txt"

    # midu2022
    midu_train_path = "./data/midu2022/preliminary_extend_train.json"
    midu_dev_path = "./data/midu2022/preliminary_val.json"
    midu_detect_tags_path = "ctc_detect_tags.txt"
    midu_correct_tags_path = "ctc_correct_tags.txt"

    # sighan13
    sighan13_train_path = "./data/sighan13/train.json"
    sighan13_dev_path = "./data/sighan13/test.json"
    sighan13_detect_tags_path = "ctc_detect_tags.txt"
    sighan13_correct_tags_path = "ctc_correct_sighan13_tags.txt"

    # sighan14
    sighan14_train_path = "./data/sighan14/train.json"
    sighan14_dev_path = "./data/sighan14/test.json"
    sighan14_detect_tags_path = "ctc_detect_tags.txt"
    sighan14_correct_tags_path = "ctc_correct_sighan14_tags.txt"

    # sighan15
    sighan15_train_path = "./data/sighan15/train.json"
    sighan15_dev_path = "./data/sighan15/test.json"
    sighan15_detect_tags_path = "ctc_detect_tags.txt"
    sighan15_correct_tags_path = "ctc_correct_sighan15_tags.txt"

    # sighan15_2
    sighan15_2_train_path = "./data/sighan15_2/train.json"
    sighan15_2_dev_path = "./data/sighan15_2/test.json"
    sighan15_2_detect_tags_path = "ctc_detect_tags.txt"
    sighan15_2_correct_tags_path = "ctc_correct_sighan15_2_tags.txt"

    # cail2022
    cail2022_train_path = "./data/cail2022/train.json"
    cail2022_dev_path = "./data/cail2022/test.json"
    cail2022_detect_tags_path = "ctc_detect_tags.txt"
    cail2022_correct_tags_path = "ctc_correct_cail2022_tags.txt"