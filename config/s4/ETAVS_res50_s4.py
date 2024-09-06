model = dict(
    type='AVS_Model',
    backbone=dict(
        type='res50',
        init_weights_path='pretrained/resnet50-19c8e357.pth'),
    vggish=dict(
        freeze_audio_extractor=True,
        pretrained_vggish_model_path='pretrained/vggish-10086976.pth',
        preprocess_audio_to_log_mel=False,
        postprocess_log_mel_with_pca=False,
        pretrained_pca_params_path=None),
    bridger=dict(
        type='TemporalFusers_res50',
        nhead=8,
        num_queries=5,
        dropout=0.1,
        feature_channel=[256, 512, 1024, 2048],
    ),
    head=dict(
        type='RefFormerHead_res50',
        scale_factors=[8, 4, 2, 1],
        d_models=[256, 512, 1024, 2048],
        nhead=8,
        pos_emb=None,
        frame = 5,
        drop_out=0.1,
        conv_dim=256,
        mask_dim=1,
        use_bias=False,
        interpolate_scale=4
    ),
    freeze=dict(
        audio_backbone=True,
        visual_backbone=True
    )
)
dataset = dict(
    train=dict(
        type='S4Dataset',
        split='train',
        anno_csv='data/Single-source/s4_meta_data.csv',
        dir_img='data/Single-source/s4_data/visual_frames',
        dir_audio_log_mel='data/Single-source/s4_data/audio_log_mel',
        dir_mask='data/Single-source/s4_data/gt_masks',
        img_size=(224, 224),
        batch_size=4),
    val=dict(
        type='S4Dataset',
        split='test',
        anno_csv='data/Single-source/s4_meta_data.csv',
        dir_img='data/Single-source/s4_data/visual_frames',
        dir_audio_log_mel='data/Single-source/s4_data/audio_log_mel',
        dir_mask='data/Single-source/s4_data/gt_masks',
        img_size=(224, 224),
        batch_size=4),
    test=dict(
        type='S4Dataset',
        split='test',
        anno_csv='data/Single-source/s4_meta_data.csv',
        dir_img='data/Single-source/s4_data/visual_frames',
        dir_audio_log_mel='data/Single-source/s4_data/audio_log_mel',
        dir_mask='data/Single-source/s4_data/gt_masks',
        img_size=(224, 224),
        batch_size=4))
optimizer = dict(
    type='AdamW',
    lr=6e-5)
loss = dict(
    weight_dict=dict(
        dice_loss=1.0,
        focal_loss=0.0),
    loss_type='dice')
process = dict(
    num_works=8,
    freeze_epochs=-1,
    train_epochs=30)
discribe = dict(
    session_name='S4',
    info='ETAVAS_res50_S4'
)
